export interface ChartValueConfig {
  id: number;
  label: string;
  formula: string;
  secondAxis: boolean;
  target: number;
  unit: string;
  color: string;
  order: number;
  factor: number;
}

const mockedChartValueConfigs: ChartValueConfig[] = [
  {
    id: 1,
    label: "AI300.PV",
    formula: "AI300.PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 2,
    label: "FIC4400.PV",
    formula: "FIC4400.PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 3,
    label: "FIC4401.PV",
    formula: "FIC4401.PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 4,
    label: "FIC4433.PV",
    formula: "FIC4433.PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 5,
    label: "PIC606A_C",
    formula: "PIC606A_C",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 6,
    label: "PIC692.MV",
    formula: "PIC692.MV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 7,
    label: "AI300.PV",
    formula: "AI300.PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 8,
    label: "PIC606A_B",
    formula: "PIC606A_B",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  },
  {
    id: 9,
    label: "TAG-3FFIC1-PIDA-PV",
    formula: "TAG-3FFIC1-PIDA-PV",
    secondAxis: false,
    target: 100.0,
    unit: "*C",
    color: "rgb(0, 31, 245)",
    order: 1,
    factor: 100.0
  }
];

export default mockedChartValueConfigs;
