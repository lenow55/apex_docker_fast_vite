// struct2ts:go.bobheadxi.dev/gobenchdata/web.ChartGroup


function ParseNumber(v: number | string, isInt = false): number {
    if (!v) return 0;
    if (typeof v === 'number') return v;
    return (isInt ? parseInt(v) : parseFloat(v)) || 0;
}

function ToObject(o: any, typeOrCfg: any = {}, child = false): any {
    if (o == null) return null;
    if (typeof o.toObject === 'function' && child) return o.toObject();

    switch (typeof o) {
        case 'string':
            return typeOrCfg === 'number' ? ParseNumber(o) : o;
        case 'boolean':
        case 'number':
            return o;
    }

    if (o instanceof Date) {
        return typeOrCfg === 'string' ? o.toISOString() : Math.floor(o.getTime() / 1000);
    }

    if (Array.isArray(o)) return o.map((v: any) => ToObject(v, typeOrCfg, true));

    const d: any = {};

    for (const k of Object.keys(o)) {
        const v: any = o[k];
        if (v === undefined) continue;
        if (v === null) continue;
        d[k] = ToObject(v, typeOrCfg[k] || {}, true);
    }

    return d;
}

class DataChart {
    id: number;
    name: string;
    count: number;
    hidden: boolean;

    constructor(data?: any) {
        const d: any = (data && typeof data === 'object') ? ToObject(data) : {};
        this.id = ('id' in d) ? d.id as number : 0;
        this.name = ('name' in d) ? d.name as string : '';
        this.count = ('count' in d) ? d.count as number : 0;
        this.hidden = false;
    }

    update(data?: any) {
        const d: any = (data && typeof data === 'object') ? ToObject(data) : {};
        this.id = ('id' in d) ? d.id as number : 0;
        this.name = ('name' in d) ? d.name as string : '';
        this.count = ('count' in d) ? d.count as number : 0;
    }

    changeVisible(): boolean { //возвращает получившееся значение
        this.hidden = (this.hidden == false);
        return this.hidden
    }

}

class Chart {
    id: number;
    name: string;
    description: string;
    data: DataChart[] | null;
    count_visible: number;

    constructor(data?: any) {
        const d: any = (data && typeof data === 'object') ? ToObject(data) : {};
        this.id = ('id' in d) ? d.id as number : 0;
        this.name = ('name' in d) ? d.name as string : '';
        this.description = ('description' in d) ? d.description as string : '';
        this.data = Array.isArray(d.data) ? d.data.map((v: any) => new DataChart(v)) : null;
        this.count_visible = Array.isArray(d.data) ? d.data.length : 0;
    }

    toObject(): any {
        const cfg: any = {};
        return ToObject(this, cfg);
    }

    generateSerie(): number[] {
        return Array.isArray(this.data) ? this.data.map((v: DataChart) => v.hidden ? 0 : v.count) : []
    }

    changeVisible(dataIndex: number): boolean {
        if (Array.isArray(this.data)) {
            const dataLink: DataChart[] = this.data;
            const dataChartLink: DataChart = dataLink[dataIndex];

            if (this.count_visible > 1 || dataChartLink.hidden == true) {
                const result: boolean = dataChartLink.changeVisible()
                result ? this.count_visible -= 1 : this.count_visible += 1;
            }
        }
        return false
    }

    getVisibleRules(): Rule4Chart[] {
        const rules: Rule4Chart[] = []

        return rules
    }

    generateCategories(): string[] {
        return Array.isArray(this.data) ? this.data.map((v: any) => v.name) : []
    }

    update(data?: any) {
        console.log("update Chart")
        const d: any = (data && typeof data === 'object') ? ToObject(data) : {};
        this.name = ('name' in d) ? d.name as string : '';
        this.description = ('description' in d) ? d.description as string : '';

        if (Array.isArray(d.data)) {
            if (Array.isArray(this.data)) {
                const currentData: DataChart[] = this.data //преобразование типа, без этого ругается
                d.data.forEach( //для каждой диаграммы
                    (inputData: DataChart) => {
                        currentData.find( //полученными данными
                            (obj: any) => obj.id == inputData.id
                        )?.update(inputData) //по условию, что id получ совпадает с id диаграммы
                    }
                )
            }
        }
        else {
            this.data = Array.isArray(d.data) ? d.data.map((v: any) => new DataChart(v)) : null;
        }
    }
}

class ChartGroup {
    name: string;
    description: string;
    charts: Chart[] | null;

    constructor(data?: any) {
        this.charts = Array.isArray(data) ? data.map((v: any) => new Chart(v)) : null;
        this.name = "Диаграммы";
        this.description = "Группа диаграмм";
    }

    toObject(): any {
        const cfg: any = {};
        return ToObject(this, cfg);
    }

    //для централлизованной обработки скрытых полей в диаграмме
    updateCharts(data?: any): void {
        //ну и нагородил,
        //короче, тут сначала проверяется, что у нас вообще есть диаграммы
        //если нет, то берём из полученных данных
        //иначе для каждой диаграммы
        console.log("update")
        if (Array.isArray(this.charts)) {
            if (Array.isArray(data)) {
                this.charts.forEach( //для каждой диаграммы
                    (v: Chart) => {
                        console.log(v)
                        v.update( //вызываем обновление данных
                            data.find( //полученными данными
                                (obj: any) => obj.id == v.id
                            ) //по условию, что id получ совпадает с id диаграммы
                        )
                    }
                )
            }
        }
        else {
            this.charts = Array.isArray(data) ? data.map((v: any) => new Chart(v)) : null;
        }
    }
}

export type Rule4Chart = {
    id_diagram: number,
    exclude_fields_id: number[],
}

export {
    // ChartDisplay,
    Chart,
    ChartGroup,
    DataChart,
    // Config,
    // Mem,
    // Benchmark,
    // Suite,
    // Run,
    // ParseDate,
    // ParseNumber,
    // FromArray,
    ToObject,
};
