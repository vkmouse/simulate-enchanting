import { autorun, observable } from "mobx";
import { EnchantedAttributeRow } from "../../../Core/Core";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";

interface IProps {
  enchantedStatsStore: EnchantedStatsStore
}

class EnchantmentStatsController {
  props: IProps;
  @observable stats: string[][] = [];

  constructor(props: IProps) {
    this.props = props;
    autorun(() => this.updateStats());
  }

  convertAttributeRowToString(attribute: EnchantedAttributeRow): string {
    const { name, value } = attribute;
    const percent = attribute.isPercentage ? '%' : '';
    const symbol = value > 0 ? '+' : value < 0 ? '-' : '';
    return `${name} ${symbol}${Math.abs(value)}${percent}`;
  }

  private updateStats() {
    this.stats = [];
    for (const attributeRows of this.props.enchantedStatsStore.stats) {
      const rows: string[] = [];
      for (const attributeRow of attributeRows) {
        rows.push(this.convertAttributeRowToString(attributeRow));
      }
      this.stats.push(rows);
    }
  }
}

export default EnchantmentStatsController;