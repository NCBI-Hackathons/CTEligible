import { Component, OnInit } from '@angular/core';
import { CRITERIAS } from '../mock-criteria';


@Component({
  selector: 'app-search-criteria',
  templateUrl: './search-criteria.component.html',
  styleUrls: ['./search-criteria.component.css']
})
export class SearchCriteriaComponent implements OnInit {

  criterias = CRITERIAS;

  constructor() {}

  ngOnInit() {
  }

}
