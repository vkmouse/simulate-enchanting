import { inject, observer } from "mobx-react";
import React from "react";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantmentSerialInfoController from "./EnchantmentSerialInfoController";
import EnchantmentSerialInfoView from "./EnchantmentSerialInfoView";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
}

interface EventProps {
  onSerialChange?: (value: NonNullable<unknown>) => void
}

@inject('enchantmentSerialStore')
@observer
class EnchantmentSerialInfoViewModel extends React.Component<IProps> {
  static defaultProps = {} as IProps;
  controller: EnchantmentSerialInfoController;
  eventProps: EventProps;

  constructor(props: IProps) {
    super(props);
    this.controller = new EnchantmentSerialInfoController(props);
    this.eventProps = {
      onSerialChange: (value: NonNullable<unknown>) => 
        this.controller.setCurrentSerialId(value as number)
    };
  }

  render() {
    return (
      <EnchantmentSerialInfoView
        serial={this.props.enchantmentSerialStore.currentSerialId}
        serialData={this.controller.getSerialData()}
        {...this.eventProps}
      />
    );
  }
}

export default EnchantmentSerialInfoViewModel;