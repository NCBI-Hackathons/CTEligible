import {searchCriteria} from './search-criteria';

export const CRITERIAS: searchCriteria[] = [
  {
		input: 'The platelet greater than or equal to 70000 platelets per cubic millimeter',
		results : [
			{
				text : "platelet greater than or equal to 70000",
				data_suggestions: "Platelet count >= 100,000/uL (transfusion independent)",
        ctep_suggestions: "None"
			}
	   ]
},
// {
//   input: 'ecog',
//   results : [
//     {
//       text : "ecog",
//       data_suggestions: "Eastern Cooperative Oncology Group (ECOG) performance status 0-1",
//       ctep_suggestions: "None"
//     }
//    ]
// },
// {
//   input: 'cancer',
//   results : [
//     {
//       text : "cancer",
//       data_suggestions: "Pathologically (histologically or cytologically) proven diagnosis of invasive breast cancer",
//       ctep_suggestions: ""
//     }
//    ]
// }
];
