import { Provider } from 'mobx-react';
import React from 'react';
import RootStore from './Data/RootStore';
import EnchantmentSerialInfoViewModel from './Presentation/Views/EnchantmentSerialInfo/EnchantmentSerialInfoViewModel';

function Title() {
  return (
    <div className='d-flex justify-content-between align-items-end my-2'>
      <span className='fs-2'>RO 附魔模擬器</span>
      <span>最後更新日期: 2022.09.22</span>
    </div>
  );
}

function App() {
  const rootStore: RootStore = new RootStore();
  
  return (
    <div className='page'>
      <div className='page__content'>
        <Title/>
        <Provider {...rootStore}>
          <EnchantmentSerialInfoViewModel />
        </Provider>
      </div>
    </div>
  );
}

export default App;
