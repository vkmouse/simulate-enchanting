import { EnchantingTerminationCondition } from "../../../Core/Core";
import EnchantableAttributeRowStore from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";
import EnchantedUserStore from "../../../Data/Store/EnchantedUserStore";
import EnchantedUser from "../../../Domain/EnchantedUser/EnchantedUser";
import ComponentData from "../../Components/ComponentData";

interface IProps {
  enchantableAttributeRowStore: EnchantableAttributeRowStore
  enchantedUserStore: EnchantedUserStore
  enchantedStatsStore: EnchantedStatsStore
}

class EnchantmentSimulationController {
  props: IProps;
  constructor(props: IProps) {
    this.props = props;
  }

  getEnchantmentMethodData(): ComponentData[] {
    return [{
      name: "次數附魔",
      value: EnchantingTerminationCondition.TimesReached
    }, {
      name: "目標附魔",
      value: EnchantingTerminationCondition.TargetReached
    }];
  }

  setEnchantmentMethod(value: EnchantingTerminationCondition) {
    this.props.enchantedUserStore.setCondition(value);
  }

  setTimes(value: number) {
    this.props.enchantedUserStore.setTimes(value);
  }

  enchant() {
    const user = new EnchantedUser(this.props.enchantableAttributeRowStore.rows);
    const result = user.enchant(this.props.enchantedUserStore);
    this.props.enchantedStatsStore.pushStats(result);
  }
}

export default EnchantmentSimulationController;