import { inject, observer } from "mobx-react";
import React from "react";
import { EnchantingTerminationCondition } from "../../../Core/Core";
import EnchantedUserStore from "../../../Data/Store/EnchantedUserStore";
import EnchantmentSimulationController from "./EnchantmentSimulationController";
import EnchantmentSimulationView from "./EnchantmentSimulationView";

interface IProps {
  enchantedUserStore: EnchantedUserStore
}

interface EventProps {
  onEnchantmentMethodChange?: (value: NonNullable<unknown>) => void
  onEnchantmentTimesChange?: (value: number) => void
}

@inject('enchantedUserStore')
@observer
class EnchantmentSimulationViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;
  controller: EnchantmentSimulationController;
  eventProps: EventProps;

  constructor(props: IProps) {
    super(props);
    this.controller = new EnchantmentSimulationController(props);
    this.eventProps = {
      onEnchantmentMethodChange: (value: NonNullable<unknown>) => 
        this.controller.setEnchantmentMethod(value as EnchantingTerminationCondition),
      onEnchantmentTimesChange: (value: number) => 
        this.controller.setTimes(value)
    };
  }

  render() {
    return (
      <EnchantmentSimulationView 
        { ...this.eventProps }
        { ...this.props.enchantedUserStore }
        enchantmentMethodData={this.controller.getEnchantmentMethodData()}
      />
    );
  }
}

export default EnchantmentSimulationViewModel;