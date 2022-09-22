import React from "react";
import ComponentData from "../../Components/ComponentData";
import Combobox from "../../Components/CustomCombobox";

interface IProps {
  serialId: NonNullable<unknown>
  serialData: ComponentData[]
  onSerialChange?: (value: NonNullable<unknown>) => void
}

class EnchantmentSerialInfoView extends React.Component<IProps> {
  render() {
    const { serialId, serialData, onSerialChange } = this.props;
    return (
      <div className="wrapper">
        <div className="wrapper__title">附魔系列</div>
        <div className='wrapper__content'>
          <Combobox 
            label="附魔系列"
            data={serialData}
            value={serialId}
            onChange={onSerialChange}
          />
        </div>
      </div>
    );
  }
}

export default EnchantmentSerialInfoView;