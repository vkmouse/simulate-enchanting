import { inject, observer } from "mobx-react";
import React from "react";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantmentSerialInfoController from "./EnchantmentSerialInfoController";
import EnchantmentSerialInfoView from "./EnchantmentSerialInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
}

@inject('enchantmentSerialStore')
@observer
class EnchantmentSerialInfoViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;
  controller: EnchantmentSerialInfoController;

  constructor(props: IProps) {
    super(props);
    this.controller = new EnchantmentSerialInfoController(props);
  }

  render() {
    return (
      <EnchantmentSerialInfoView/>
    );
  }
}

export default EnchantmentSerialInfoViewModel;