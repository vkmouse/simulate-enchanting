import React from "react";
import ComponentData from "../../Components/ComponentData";
import Button from "../../Components/CustomButton";
import TabPanel from "../../Components/CustomTabPanel";
import ToggleButton from "../../Components/CustomToggleButton";
import TextField from "../../Components/NumberTextField";

interface IProps {
  enchantmentMethodData: ComponentData[]
  condition: NonNullable<unknown>
  times: number
  onEnchantmentMethodChange?: (value: NonNullable<unknown>) => void
  onEnchantmentTimesChange?: (value: number) => void
}

class EnchantmentSimulationView extends React.Component<IProps> {
  render() {
    const { 
      enchantmentMethodData, 
      condition,
      times,
      onEnchantmentMethodChange,
      onEnchantmentTimesChange
    } = this.props;

    return (
      <div className='wrapper'>
        <div className='wrapper__title'>模擬附魔</div>
        <div className='wrapper__content'>
          <div className='wrapper__row'>
            <ToggleButton
              data={enchantmentMethodData}
              value={condition}
              toggleButtonProps={{ sx: { fontSize: 16, lineHeight: 1.2 } }}
              onChange={onEnchantmentMethodChange}
            />
            <Button label='開始附魔'/>
          </div>
          <TabPanel 
            index={enchantmentMethodData[0].value} 
            value={condition}
          >
            <TextField 
              label={"附魔次數"} 
              value={times} 
              onChange={onEnchantmentTimesChange}
              maxValue={9999}
            />
          </TabPanel>
          <TabPanel 
            index={enchantmentMethodData[1].value} 
            value={condition}
          >
            Page 2
          </TabPanel>
        </div>
      </div>
    );
  }
}

export default EnchantmentSimulationView;