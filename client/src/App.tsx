import { Provider } from 'mobx-react';
import React from 'react';
import './App.css';
import RootStore from './Data/RootStore';
import EnchantmentSerialInfoViewModel from './Presentation/Views/EnchantmentSerialInfo/EnchantmentSerialInfoViewModel';
import EnchantableAttributeInfoViewModel from './Presentation/Views/EnchantableAttributeInfo/EnchantableAttributeInfoViewModel';
import Title from './Presentation/Components/Title';
import EnchantmentSimulationViewModel from './Presentation/Views/EnchantmentSimulation/EnchantmentSimulationViewModel';

function App() {
  const rootStore: RootStore = new RootStore();
  return (
    <div className='page'>
      <div className='page__content'>
        <Title />
        <Provider {...rootStore}>
          <EnchantmentSerialInfoViewModel />
          <EnchantableAttributeInfoViewModel />
          <EnchantmentSimulationViewModel />
        </Provider>
      </div>
    </div>
  );
}

export default App;
