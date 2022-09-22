import { Box } from '@mui/material';
import React from 'react';
import ComponentData from '../../Components/ComponentData';
import Combobox from '../../Components/CustomCombobox';

interface IProps {
  serialId: NonNullable<unknown>
  serialDescription: string
  serialUrl: string
  serialData: ComponentData[]
  onSerialChange?: (value: NonNullable<unknown>) => void
}

class EnchantmentSerialInfoView extends React.Component<IProps> {
  render() {
    const { 
      serialId, 
      serialDescription,
      serialUrl,
      serialData,
      onSerialChange 
    } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔系列</div>
        <div className='wrapper__content'>
          <div>
            <Combobox 
              label='系列名稱'
              data={serialData}
              value={serialId}
              onChange={onSerialChange}
            />
          </div>
          <Box sx={{ margin: '0.5em', marginTop: '1.0em' }}>
            <Box sx={{ fontWeight: 'bold', marginTop: '0.5em' }}>內容說明</Box>
            <Box sx={{ marginTop: '0.5em' }}>{serialDescription}</Box>
            <Box sx={{ marginTop: '0.5em' }}><a href={serialUrl}>前往官方網站</a></Box>
          </Box>
        </div>
      </div>
    );
  }
}

export default EnchantmentSerialInfoView;