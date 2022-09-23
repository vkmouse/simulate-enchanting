import { inject, observer } from "mobx-react";
import React from "react";
import EnchantableAttributeRowStore from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantableAttributeInfoView from "./EnchantableAttributeInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
  enchantableAttributeRowStore: EnchantableAttributeRowStore
}

interface IState {
  rowNumber: number
  onRowNumberChange?: (value: NonNullable<unknown>) => void
}

@inject('enchantmentSerialStore', 'enchantableAttributeRowStore')
@observer
class EnchantableAttributeInfoViewModel extends React.Component<IProps, IState> {
  static defaultProps = {} as IProps;

  constructor(props: IProps) {
    super(props);
    this.state = {
      rowNumber: 1,
      onRowNumberChange: p => this.setState({ rowNumber: p as number })
    };
  }

  getRowProbability() {
    const { enchantableAttributeRowStore } = this.props;
    const found = enchantableAttributeRowStore.rows.find(p => p.rowNumber === this.state.rowNumber);
    if (found !== undefined) {
      return found.probability * 100;
    } else {
      return 0;
    }
  }

  render() {
    return (
      <EnchantableAttributeInfoView
        rowQuantity={this.props.enchantableAttributeRowStore.rows.length}
        rowProbability={this.getRowProbability()}
        { ...this.state }
      />
    );
  }
}

export default EnchantableAttributeInfoViewModel;