import { EnchantingTerminationCondition } from "../../../Core/Core";
import EnchantedUserStore from "../../../Data/Store/EnchantedUserStore";
import ComponentData from "../../Components/ComponentData";

interface IProps {
  enchantedUserStore: EnchantedUserStore
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
}

export default EnchantmentSimulationController;