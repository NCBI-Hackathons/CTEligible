import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from './app.component';
import {SearchItemsComponent} from './search-items/search-items.component';
import { ResultsComponent }      from './results/results.component';
import { AboutComponent }      from './about/about.component';

const routes: Routes = [
  { path: '', redirectTo: '/about', pathMatch: 'full' },
  { path: 'about', component: AboutComponent },
  { path: 'search_criteria', component: SearchItemsComponent },
  { path: 'results', component: ResultsComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {


}
