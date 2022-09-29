import React from "react";
import { EnchantingTerminationCondition } from "../../../Core/Core";
import EnchantmentSimulationView from "./EnchantmentSimulationView";

class EnchantmentSimulationViewModel extends React.Component {
  render() {
    return (
      <EnchantmentSimulationView 
        enchantmentMethodData={[{
          name: "次數附魔",
          value: EnchantingTerminationCondition.TimesReached
        }, {
          name: "目標附魔",
          value: EnchantingTerminationCondition.TargetReached
        }]}
        enchantmentMethod={EnchantingTerminationCondition.TimesReached}
      />
    );
  }
}

export default EnchantmentSimulationViewModel;