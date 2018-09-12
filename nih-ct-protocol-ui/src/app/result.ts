

export class Result {

    constructor(
            public total: number=0,
            public max_score: number=0,
            public hits: Hit[]=[],

        ){}
}

export class Hit {

    constructor(
            public _index: string="",
            public _type: string="",
            public _score: number=0,
            public highlight: Highlight=new Highlight(),
        ){}
}

export class Highlight {

    constructor(
            public value: string[]=[],
        ){}
}
