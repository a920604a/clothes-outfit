import { FunctionComponent } from "react";

export type NavigationFooterType = {
  className?: string;
};

const NavigationFooter: FunctionComponent<NavigationFooterType> = ({
  className = "",
}) => {
  return (
    <footer
      className={`self-stretch shadow-[0px_4px_4px_rgba(0,_0,_0,_0.25)] bg-white overflow-hidden flex flex-col items-start justify-start pt-px pb-[71px] pr-[79px] pl-20 box-border gap-[46px] max-w-full text-left text-xl text-black font-arimo-hebrew-subset-italic mq825:gap-[23px] mq825:pl-10 mq825:pr-[39px] mq825:box-border ${className}`}
    >
      <div className="self-stretch h-px relative box-border border-t-[1px] border-solid border-gainsboro" />
      <div className="w-0 h-[30px] hidden" />
      <div className="w-[1261px] flex flex-row items-start justify-between gap-[20px] max-w-full mq675:flex-wrap">
        <div className="flex flex-col items-start justify-start gap-[4px]">
          <h1 className="m-0 relative text-21xl leading-[150%] font-normal font-damion mq825:text-13xl mq825:leading-[48px] mq450:text-5xl mq450:leading-[36px]">
            Colors to go
          </h1>
          <i className="relative leading-[150%] inline-block min-w-[126px] mq450:text-base mq450:leading-[24px]">
            ccClub project
          </i>
          <i className="relative leading-[150%] text-darkgray mq450:text-base mq450:leading-[24px]">
            Tim、Jennie、Ellie
          </i>
        </div>
        <div className="w-[200px] flex flex-col items-start justify-start pt-3 px-0 pb-0 box-border">
          <div className="self-stretch flex flex-col items-start justify-start">
            <i className="self-stretch relative leading-[150%] z-[1] mq450:text-base mq450:leading-[24px]">
              Cooperate with Beams
            </i>
            <div className="self-stretch flex flex-row items-start justify-end">
              <img
                className="h-[103px] w-[143px] relative object-cover z-[1]"
                loading="lazy"
                alt=""
                src="/beams.png"
              />
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default NavigationFooter;