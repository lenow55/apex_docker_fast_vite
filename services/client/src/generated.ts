// struct2ts:go.bobheadxi.dev/gobenchdata/web.ChartGroup
class ChartGroup {
    name: string;
    description: string;
    charts: Chart[] | null;

    constructor(data?: any) {
        const d: any = (data && typeof data === 'object') ? ToObject(data) : {};
        this.name = ('name' in d) ? d.name as string : '';
        this.description = ('description' in d) ? d.description as string : '';
        this.charts = Array.isArray(d.charts) ? d.charts.map((v: any) => new Chart(v)) : null;
    }

    toObject(): any {
        const cfg: any = {};
        return ToObject(this, cfg);
    }
}

export {
    // ChartDisplay,
    // Chart,
    ChartGroup,
    // Config,
    // Mem,
    // Benchmark,
    // Suite,
    // Run,
    // ParseDate,
    // ParseNumber,
    // FromArray,
    // ToObject,
};
