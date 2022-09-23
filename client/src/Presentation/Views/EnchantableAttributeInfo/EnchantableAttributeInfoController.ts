import { action, autorun, makeObservable, observable } from "mobx";
import EnchantableAttributeRowStore from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import ComponentData from "../../Components/ComponentData";
import EnchantableAttributeInfo from "./EnchantableAttributeInfo";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
  enchantableAttributeRowStore: EnchantableAttributeRowStore
}

class EnchantableAttributeInfoController {
  private props: IProps;
  
  @observable attributes: EnchantableAttributeInfo[] = [];
  @observable rowData: ComponentData[] = [];
  @observable rowNumber = 0;
  @observable rowProbability = 0;

  constructor(props: IProps) {
    makeObservable(this);
    this.props = props;
    autorun(() => {
      this.updateRow(this.getFirstRow());
    });
  }

  setRowNumber(value: number) {
    if (this.containRow(value)) {
      this.updateRow(value);
    }
  }

  @action private updateRow(value: number) {
    this.rowNumber = value;
    this.rowData = this.getRowData();
    this.rowProbability = this.getRowProbability();
    this.attributes = this.getAttibutes();
  }

  private getAttibutes() {
    const found = this.findRow(this.rowNumber);
    if (found !== undefined) {
      return found.enchantableAttributes.map(p => {
        const probability: string = 
          (Math.round(p.probability * 100 * 1000) / 1000).toString();
        return {
          name: p.name,
          probability
        };
      });
    } else {
      return [];
    }
  }

  private getRowData() {
    const rowQuantity = this.props.enchantableAttributeRowStore.rows.length;
    const array = [
      { name: '第一欄', value: 1 },
      { name: '第二欄', value: 2 },
      { name: '第三欄', value: 3 },
    ];
    return array.filter(p => rowQuantity >= p.value);
  }

  private getRowProbability() {
    const found = this.findRow(this.rowNumber);
    if (found !== undefined) {
      return found.probability * 100;
    } else {
      return 0;
    }
  }

  private getFirstRow() {
    if (this.props.enchantableAttributeRowStore.rows.length > 0) {
      return Math.min(...this.props.enchantableAttributeRowStore.rows.map(p => p.rowNumber));
    } else {
      return 0;
    }
  }

  private containRow(rowNumber: number) {
    return this.findRow(rowNumber) !== undefined;
  }

  private findRow(rowNumber: number) {
    return this.props.enchantableAttributeRowStore.rows.find(p => p.rowNumber === rowNumber);
  }
}

export default EnchantableAttributeInfoController;