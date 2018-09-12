@Injectable()
export class CriteriaService {
  apiUrl = '/get-suggestion/';  // URL to web api
  private handleError: HandleError;

  constructor(
    private http: HttpClient,
    httpErrorHandler: HttpErrorHandler) {
    this.handleError = httpErrorHandler.createHandleError('CriteriaService');
  }

  //////// Save methods //////////

  /** POST: add a new hero to the database */
  addInput (criteria: Criteria): Observable<Criteria> {
    return this.http.post<Criteria>(this.apiUrl, criteria, httpOptions)
      .pipe(
        catchError(this.handleError('addInput', criteria))
      );
  }

}
