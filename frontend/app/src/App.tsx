import React from 'react';
import NavigationFooter from '@/components/NavigationFooter';
import LocationStyle from './components/LocationStyle';

const App: React.FC = () => {


  return (
    <div className="w-full relative bg-white overflow-hidden flex flex-col items-start justify-start pt-0 px-0 pb-[37px] box-border gap-[78px] leading-[normal] tracking-[normal] mq825:gap-[39px] mq450:gap-[19px]">
      <header className="self-stretch shadow-[0px_4px_4px_rgba(0,_0,_0,_0.25)] bg-white overflow-hidden flex flex-row items-end justify-between py-px pr-[135px] pl-[101px] gap-[20px] text-left text-[54px] text-black font-damion mq825:pl-[50px] mq825:pr-[67px] mq825:box-border mq450:pl-5 mq450:pr-5 mq450:box-border">
        <h1 className="m-0 relative text-inherit leading-[150%] font-normal font-inherit [text-shadow:1px_0_0_#000,_0_1px_0_#000,_-1px_0_0_#000,_0_-1px_0_#000]">
          <p className="m-0">&nbsp;</p>
          <p className="m-0">Colors to go</p>
        </h1>
        <div className="h-[78px] w-[200px] flex flex-col items-start justify-start text-xl font-arimo-hebrew-subset-italic">
          <i className="self-stretch relative leading-[150%] whitespace-nowrap">
            Cooperate with Beams
          </i>
        </div>
      </header>
      <main className="self-stretch flex flex-row items-start justify-center pt-0 pb-[18px] pr-[30px] pl-5 box-border max-w-full">
        <LocationStyle />
      </main>
      <NavigationFooter />
    </div>
  );
};

export default App;
