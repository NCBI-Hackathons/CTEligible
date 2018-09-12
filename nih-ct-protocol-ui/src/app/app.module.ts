import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatInputModule} from '@angular/material/input';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatButtonModule} from '@angular/material/button';

import { AppComponent } from './app.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule }   from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import {MatCheckboxModule} from '@angular/material/checkbox';
import { HttpClientModule }    from '@angular/common/http';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatListModule} from '@angular/material/list';
import { FroalaEditorModule, FroalaViewModule } from 'angular-froala-wysiwyg';
import { SearchCriteriaComponent } from './search-criteria/search-criteria.component';
import { SearchItemsComponent } from './search-items/search-items.component';
import { AppRoutingModule } from './/app-routing.module';
import { ResultsComponent } from './results/results.component';
import {MatExpansionModule} from '@angular/material/expansion';
import { AboutComponent } from './about/about.component';
import { HttpModule } from '@angular/http';



@NgModule({
  declarations: [
    AppComponent,
    SearchCriteriaComponent,
    SearchItemsComponent,
    ResultsComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    MatInputModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatFormFieldModule,
    FormsModule,
    HttpClientModule,
    MatIconModule,
    MatCheckboxModule,
    MatGridListModule,
    MatListModule,
    FroalaEditorModule.forRoot(),
    FroalaViewModule.forRoot(),
    AppRoutingModule,
    MatExpansionModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent,SearchItemsComponent]
})
export class AppModule { }
