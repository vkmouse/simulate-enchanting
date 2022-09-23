import { inject, observer } from "mobx-react";
import React from "react";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantableAttributeInfoView from "./EnchantableAttributeInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
}

@inject('enchantmentSerialStore')
@observer
class EnchantableAttributeInfoViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;

  constructor(props: IProps) {
    super(props);
  }

  render() {
    return (
      <EnchantableAttributeInfoView
      />
    );
  }
}

export default EnchantableAttributeInfoViewModel;