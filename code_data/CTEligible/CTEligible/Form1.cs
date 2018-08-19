using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.Entity.Infrastructure;

namespace CTEligible
{
    public partial class ctEligible : Form
    {
        public ctEligible()
        {
            InitializeComponent();
        }

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            DialogResult result = ofd.ShowDialog(); // Show the dialog.
            if (result == DialogResult.OK) // Test result.
            {
                string file = ofd.FileName;
                txtFileName.Text = file;

                try
                {
                    string text = File.ReadAllText(file);
                    rtContent.Text = text;
                }
                catch (IOException)
                {
                }
            }
        }

        private void btnMatch_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(rtContent.Text))
            {
                string txt = rtContent.Text;
                string criteria = string.Empty;
                bool inc = false;
                List<string> incCriteria = new List<string>();
                List<string> excCriteria = new List<string>();

                StringBuilder sb = new StringBuilder();
                foreach (string line in txt.Split(new string[] { "\r\n", "\n" }, StringSplitOptions.None))
                {
                    if (line.Contains("Inclusion"))
                    {
                        criteria = "Inclusion";
                        inc = true;
                        continue;
                    }
                    if (line.Contains("Exclusion"))
                    {
                        criteria = "Exclusion";
                        inc = false;
                        continue;
                    }

                    if (inc == true)
                    {
                        if (!string.IsNullOrEmpty(line))
                        {
                            incCriteria.Add(line);
                        }
                    }
                    else
                    {
                        if (!string.IsNullOrEmpty(line))
                        {
                            excCriteria.Add(line);
                        }
                    }

                }

                if (incCriteria.Count > 0)
                {
                    string query = $"select nci_id from [NCIT].[dbo].[NCI_Trials] where ([inclusion_indicaInclusionor]='Inclusion') and ";

                    string queryExt = string.Empty;
                    foreach (string str in incCriteria)
                    {
                        string strinc = string.Empty;
                        strinc = str.Split(' ')[0];
                        queryExt = queryExt + $"([description] like '%{strinc}%') or ";
                    }

                    int place = queryExt.LastIndexOf("or");
                    string result = string.Empty;
                    if (place != -1)
                    {
                        result = queryExt.Remove(place, 2).Insert(place, "");
                    }
                    queryExt = "(" + result + ")";
                    query = query + queryExt;

                    richTextBox1.Text = query;

                    List<string> lsIDs = new List<string>();
                    lsIDs = FetchData(query);

                    foreach(string strID in lsIDs)
                    {
                        lbTerms.Items.Add(strID);
                    }
                }
            }
        }

        public List<string> FetchData(string query)
        {
            List<string> lsSM = new List<string>();

            try
            {
                using (var cdContext = new NCITEntities1())
                {
                    //var db = cdContext.Set<SearchModel>();
                    cdContext.Database.CommandTimeout = 10800;
                    var searchContext = ((IObjectContextAdapter)cdContext).ObjectContext;
                    var results = searchContext.ExecuteStoreQuery<string>(query);
                    lsSM = results.ToList<string>();
                }
            }
            catch (Exception ex)
            {
                
            }

            return lsSM;
        }
    }
}
