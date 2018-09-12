import { Component, OnInit } from '@angular/core';
import {Result} from './result';
import {CriteriaService} from './criteria.service';


@Component({
  selector: 'app-search-items',
  templateUrl: './search-items.component.html',
  styleUrls: ['./search-items.component.css']
})
export class SearchItemsComponent implements OnInit {
    userInput: string;
    inputs = [];

public options: Object = {
  placeholderText: 'Enter Protocol Input',
  charCounterCount: false,
  toolbarButtons: ['bold', 'italic', 'underline','formatUL'],
  quickInsertTags: []
    }

    addNew(){
      this.userInput = '';
      this.CriteriaService.addInput(userInput)
        .subscribe(this.userInput => this.userInput.push(inputs));
      }




  constructor() { }



  ngOnInit() {


  }

}
