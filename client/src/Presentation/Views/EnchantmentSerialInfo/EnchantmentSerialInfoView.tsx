import React from "react";
import ComponentData from "../../Components/ComponentData";
import Combobox from "../../Components/CustomCombobox";

interface IProps {
  serial: NonNullable<unknown>
  serialData: ComponentData[]
  onSerialChange?: (value: NonNullable<unknown>) => void
  onNumSamplesChange?: (value: number) => void
  onStartSimulationClick?: () => void
}

class EnchantmentSerialInfoView extends React.Component<IProps> {
  render() {
    const { serial, serialData, onSerialChange } = this.props;
    return (
      <div className="wrapper">
        <div className="wrapper__title">附魔系列</div>
        <div className='wrapper__content'>
          <Combobox 
            label="附魔系列"
            data={serialData}
            value={serial}
            onChange={onSerialChange}
          />
        </div>
      </div>
    );
  }
}

export default EnchantmentSerialInfoView;