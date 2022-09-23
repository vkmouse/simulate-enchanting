import { inject, observer } from "mobx-react";
import React from "react";
import EnchantableAttributeRowStore from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantableAttributeInfoView from "./EnchantableAttributeInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
  enchantableAttributeRowStore: EnchantableAttributeRowStore
}

@inject('enchantmentSerialStore', 'enchantableAttributeRowStore')
@observer
class EnchantableAttributeInfoViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;

  constructor(props: IProps) {
    super(props);
  }

  render() {
    return (
      <EnchantableAttributeInfoView
        rowQuantity={this.props.enchantableAttributeRowStore.rows.length}
      />
    );
  }
}

export default EnchantableAttributeInfoViewModel;