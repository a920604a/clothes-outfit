import{ useMemo,  type CSSProperties, FunctionComponent } from "react";

export type GalleryItemRowType = {
  className?: string;
  image?: string;
  description?: string;
  postUrl?: string;
  propWidth?: CSSProperties["width"];
};

type ImageData = {
  imageUrl: string;
  postUrl: string;
};

type GalleryItemRowProps = {
  images: ImageData[]; // 定义接受的 props 类型
};

// GalleryItemRow 子組件
const GalleryItemRow: FunctionComponent<GalleryItemRowType> = ({
  className = "",
  image,
  description = "Beams",
  postUrl,
  propWidth,
}) => {
  const galleryItemRowStyle: CSSProperties = useMemo(() => {
    return {
      width: propWidth,
    };
  }, [propWidth]);

  return (
    <div
      className={`h-[424px] flex flex-col items-start justify-start gap-[14px] max-w-full text-left text-xl text-black font-kreon ${className}`}
      style={galleryItemRowStyle}
    >
      <a href={postUrl} target="_blank" rel="noopener noreferrer">
        <img
          className="self-stretch flex-1 relative rounded-lg max-w-full overflow-hidden max-h-full object-cover"
          alt={description}
          src={image}
        />
      </a>
      <div className="flex flex-row items-start justify-start py-0 px-px">
        <div className="relative leading-[150%] inline-block min-w-[54px] mq450:text-base mq450:leading-[24px]">
          {description}
        </div>
      </div>
    </div>
  );
};

// 主組件
const GalleryComponent: FunctionComponent<GalleryItemRowProps> = ({images}) => {

  return (
    <div className="self-stretch grid gap-[26px] max-w-full overflow-x-auto grid-cols-3">
      {images.map((imageData, index) => (
        <GalleryItemRow
          key={index}
          className="custom-class"
          image={imageData.imageUrl}
          propWidth="324px"
          description="Beams"
          postUrl={`https://www.beams.tw/${imageData.postUrl}`}
        />
      ))}
    </div>
  );
};

export default GalleryComponent;
