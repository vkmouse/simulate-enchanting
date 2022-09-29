import { inject, observer } from "mobx-react";
import React from "react";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";
import EnchantmentStatsController from "./EnchantmentStatsController";
import EnchantmentStatsView from "./EnchantmentStatsView";

interface IProps {
  enchantedStatsStore: EnchantedStatsStore
}

@inject('enchantedStatsStore')
@observer
class EnchantmentStatsViewModel  extends React.Component {
  static defaultProps = {} as IProps;
  controller: EnchantmentStatsController;

  constructor(props: IProps) {
    super(props);
    this.controller = new EnchantmentStatsController(props);
  }

  render() {
    return (
      <EnchantmentStatsView 
        { ...this.controller }
      />
    );
  }
}

export default EnchantmentStatsViewModel;