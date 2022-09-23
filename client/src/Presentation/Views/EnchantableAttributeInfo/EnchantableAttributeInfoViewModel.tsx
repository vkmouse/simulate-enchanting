import { inject, observer } from "mobx-react";
import React from "react";
import EnchantableAttributeRowStore from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantableAttributeInfoController from "./EnchantableAttributeInfoController";
import EnchantableAttributeInfoView from "./EnchantableAttributeInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
  enchantableAttributeRowStore: EnchantableAttributeRowStore
}

interface EventProps {
  onRowNumberChange?: (value: NonNullable<unknown>) => void
}

@inject('enchantmentSerialStore', 'enchantableAttributeRowStore')
@observer
class EnchantableAttributeInfoViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;
  controller: EnchantableAttributeInfoController;
  eventProps: EventProps;

  constructor(props: IProps) {
    super(props);
    this.controller = new EnchantableAttributeInfoController(props);
    this.eventProps = {
      onRowNumberChange: (value: NonNullable<unknown>) => 
        this.controller.setRowNumber(value as number)
    };
  }

  render() {
    return (
      <EnchantableAttributeInfoView
        { ...this.controller }
        { ...this.eventProps }
      />
    );
  }
}

export default EnchantableAttributeInfoViewModel;