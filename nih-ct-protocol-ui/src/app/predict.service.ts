import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import {Result} from './result';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  private url ="http://10.0.0.38:9200/template/_search";
  private httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

  constructor(private http: HttpClient) { }

  predict(type:string, criteria:string): Observable<any>{

	let m = { 
    "min_score": 0.1,
    "query": { 
      "match": { 
        "value": "xsxsx" 
      } 
    }, 
    "highlight" : { 
      "pre_tags" : ["<mark>"], 
      "post_tags" : ["</mark>"], 
      "fields" : { 
        "value" : {} 
      } 
    } 
  };
	m.query.match.value = criteria;

	return this.http.post<any>(this.url,m,this.httpOptions).pipe(
      catchError(this.handleError('predict', new Result()))
    );
  	
  }

private handleError<T> (operation = 'operation', result?: T) {
  return (error: any): Observable<T> => {

    console.error(error); 

    return of(result as T);
  };
}

}
