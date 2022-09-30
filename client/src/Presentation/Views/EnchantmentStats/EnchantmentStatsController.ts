import { action, autorun, makeObservable, observable } from "mobx";
import { EnchantedAttributeRow } from "../../../Core/Core";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
  enchantedStatsStore: EnchantedStatsStore
}

class EnchantmentStatsController {
  private props: IProps;

  @observable stats: string[][] = [];

  constructor(props: IProps) {
    makeObservable(this);
    this.props = props;
    autorun(() => {
      this.updateStats(this.props.enchantedStatsStore.stats);
    });
    autorun(() => {
      this.props.enchantmentSerialStore.serialId; // auto run when serialId change
      this.props.enchantedStatsStore.clear();
    });
  }

  convertAttributeRowToString(attribute: EnchantedAttributeRow): string {
    const { name, value } = attribute;
    const percent = attribute.isPercentage ? '%' : '';
    const symbol = value > 0 ? '+' : value < 0 ? '-' : '';
    return `${name} ${symbol}${Math.abs(value)}${percent}`;
  }

  @action private updateStats(newStats: EnchantedAttributeRow[][]) {
    const stats = [];
    for (const attributeRows of newStats) {
      const rows: string[] = [];
      for (const attributeRow of attributeRows) {
        rows.push(this.convertAttributeRowToString(attributeRow));
      }
      stats.push(rows);
    }
    this.stats = stats;
  }
}

export default EnchantmentStatsController;