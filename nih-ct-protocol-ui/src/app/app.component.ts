import { Component } from '@angular/core';
import {PredictService} from './predict.service';
import {Result} from './result';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  result=null;
  text="";
  suggestion='';
  score =0



  constructor(private predictService: PredictService){}

  onSubmit(){

    this.suggestion="sfsfs";
    this.score=9;

	this.predictService.predict("sfsf",this.text)
        .subscribe(res => {
		this.result = res;
    if(res.hits.total>0)
    {
      this.suggestion="";

      res.hits.hits.forEach(h=>{

        h._source.value.split(" ").forEach(w=>{

        if(this.text.indexOf(w)>-1)
        {
          this.suggestion=this.suggestion+ " "+w;
        }
        else{
          this.suggestion=this.suggestion+" <mark>"+w+"</mark>";
        }

        
      });

        this.suggestion = this.suggestion +" SCORE: " + ((h._score - 0) / (1 - 0)) + "</br>" + "</br>";


      });

      
      

      
    }
    


		});


  	
  	
  }




}
