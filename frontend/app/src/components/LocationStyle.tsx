import { FunctionComponent, useEffect, useState } from "react";
import GalleryItemRow from "./GalleryItemRow";
import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"
import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import axios from "axios";
export type LocationStyleType = {
  className?: string;
};

type ImageData = {
  imageUrl: string;
  postUrl: string;
  dataNumber: string;
};


const LocationStyle: FunctionComponent<LocationStyleType> = ({
  className = "",
}) => {

  const colors = [
    { name: 'black', bgColor: 'data-[state=on]:bg-black', dimmedColor: 'data-[state=off]:bg-black/70' },
    { name: 'white', bgColor: 'data-[state=on]:bg-white', dimmedColor: 'data-[state=off]:bg-white/70', extraClass: 'box-border border-[1px] border-solid border-gray' },
    { name: 'gray', bgColor: 'data-[state=on]:bg-gray-100', dimmedColor: 'data-[state=off]:bg-gray-100/70' },
    { name: 'silver', bgColor: 'data-[state=on]:bg-silver', dimmedColor: 'data-[state=off]:bg-silver/70' },
    { name: 'blue', bgColor: 'data-[state=on]:bg-darkslateblue', dimmedColor: 'data-[state=off]:bg-darkslateblue/70' },
    { name: 'red', bgColor: 'data-[state=on]:bg-crimson', dimmedColor: 'data-[state=off]:bg-crimson/70' },
    { name: 'brown', bgColor: 'data-[state=on]:bg-saddlebrown', dimmedColor: 'data-[state=off]:bg-saddlebrown/70' },
    { name: 'beige', bgColor: 'data-[state=on]:bg-khaki', dimmedColor: 'data-[state=off]:bg-khaki/70' },
    { name: 'green', bgColor: 'data-[state=on]:bg-forestgreen', dimmedColor: 'data-[state=off]:bg-forestgreen/70' },
    { name: 'orange', bgColor: 'data-[state=on]:bg-orange', dimmedColor: 'data-[state=off]:bg-orange/70' }
  ];

  const stylesColorsMap: { [key: string]: string[] } = {
    '簡約': ['black', 'white', 'gray', 'silver', 'blue'],
    '工業': ['gray', 'black', 'silver', 'red', 'brown', 'beige', 'green'],
    '復古': ['brown', 'beige', 'green', 'white'],
    '庭園': ['green', 'beige', 'brown', 'white'],
    '南洋': ['orange', 'green', 'beige', 'brown', 'white'],
    '地中海': ['blue', 'white', 'green', 'beige', 'brown'],
    '波西米雅': ['red', 'blue', 'beige', 'brown', 'green']
  };

  const [selectedColor, setSelectedColor] = useState<string[]>([]);
  const [selectedGender, setSelectedGender] = useState<string | null>(null);
  const [newColors, setNewColors] = useState<string[]>([]);
  const [images, setImages] = useState<ImageData[]>([]);
  const [page, setPage] = useState<number>(1);
  const [item, setItem] = useState<string>("Popularity")


  const handleStyleChange = (styles: string[]) => {
    const calculatedColors = styles.flatMap(style => stylesColorsMap[style] || []);
    setNewColors(Array.from(new Set(calculatedColors)));
  };
  const filteredColors = newColors.length > 0 ? colors.filter(color => newColors.includes(color.name)) : colors;
  console.log("filteredColors", filteredColors);

  const handleColorChange = (color: string | string[]) => {
    setSelectedColor(prevColors => {
      if (typeof color === 'string') {
        return [color];
      } else if (Array.isArray(color)) {
        return [...color];
      }
      return prevColors;
    });
    setItem("All Item");
  };
  const handleGenderChange = (gender: string) => {
    setSelectedGender(gender);
    setItem("All Item");
  };

  useEffect(() => {
    const fetchImages = async () => {
      const colorParams = selectedColor.join(',');
      const genderParam = (selectedGender?.includes("M") || selectedGender?.includes("W")) ? `&gender=${selectedGender}` : '';
      console.log("colorParams", colorParams);

      try {
        const response = await axios.get<{
          image_url: string[];
          post_url: string[];
          all_items: string;
        }>(`http://localhost:8080/api/images?page=${page}&pageSize=12&color=${colorParams}${genderParam}`);

        const data = response.data;
        const formattedData: ImageData[] = data.image_url.map((url, index) => ({
          imageUrl: url,
          postUrl: data.post_url[index],
          dataNumber: data.all_items
        }));

        setImages(formattedData);
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    };

    fetchImages();
  }, [selectedColor, selectedGender, page]);
  return (
    <section
      className={`w-[1090px] flex flex-col items-start justify-start gap-[49px] max-w-full text-left text-xl text-darkgray font-noto-sans-cjk-tc mq675:gap-[24px] ${className}`}
    >
      <div className="w-[654px] flex flex-col items-start justify-start gap-[30px] max-w-full">
        <div className="self-stretch flex flex-row flex-wrap items-start justify-start gap-[20px] max-w-full">
          <div className="flex-1 flex flex-col items-start justify-start gap-[30px] min-w-[269px] max-w-full">
            <div className="self-stretch flex flex-row items-start justify-start gap-[9px] mq450:flex-wrap">
              <div className="relative leading-[150%] font-medium text-black whitespace-nowrap mq450:text-base mq450:leading-[24px]">
                ① 選擇地點的風格｜
              </div>
              <ToggleGroup
                type="multiple"
                className="flex flex-row items-start justify-start gap-[9px]"
                onValueChange={(value) => handleStyleChange(value)}
              >
                {['簡約', '工業', '復古', '庭園', '南洋', '地中海', '波西米雅'].map((style, index) => (
                  <ToggleGroupItem
                    key={index}
                    value={style}
                    aria-label={style}
                    className="flex items-center justify-center px-2 py-1 min-w-[40px] text-gray mq450:text-base mq450:leading-[24px]"
                  >
                    {style}
                  </ToggleGroupItem>
                ))}
              </ToggleGroup>
            </div>
            <div className="flex flex-row items-start justify-start gap-[9px] max-w-full mq450:flex-wrap">
              <div className="flex items-center leading-[150%] mt-1.5 font-medium text-black min-w-[125px] mq450:text-base mq450:leading-[24px]">
                <span>② 選擇性別｜</span>
              </div>
              <ToggleGroup
                type="single"
                className="flex flex-row items-center justify-start gap-[20px]"
                onValueChange={(value) => handleGenderChange(value)}
              >
                {['M', 'W', 'no-preference'].map((gender, index) => (
                  <ToggleGroupItem
                    key={index}
                    value={gender}
                    aria-label={gender}
                    className="text-gray text-center cursor-pointer mq450:text-base mq450:leading-[24px]"
                  >
                    {gender === 'M' ? '男性' : gender === 'W' ? '女性' : '不限性別'}
                  </ToggleGroupItem>
                ))}
              </ToggleGroup>
            </div>
          </div>
        </div>
        <div className="flex flex-row items-end justify-start gap-[9px] max-w-full text-black mq675:flex-wrap">
          <div className="relative leading-[150%] font-medium inline-block min-w-[125px] mq450:text-base mq450:leading-[24px]">
            ③ 選擇顏色｜
          </div>
          <ToggleGroup
            type="multiple"
            className="flex flex-row items-center justify-start gap-[20px]"
            onValueChange={(value) => handleColorChange(value)}
          >
            {filteredColors.map((color, index) => {
              return (
                <div key={index} className="flex flex-col items-start justify-end pt-0 pb-0.5 pr-[11px] pl-0">
                  <ToggleGroupItem
                    className = {` w-[25px] h-[25px] rounded-[50%] ${selectedColor.includes(color.name) ? color.bgColor : color.dimmedColor} ${color.extraClass || ''}`}
                  value={color.name}
                  />
                </div>
              )
            })}
          </ToggleGroup>
        </div>
      </div>
      <div className="self-stretch flex flex-row items-start justify-start py-0 pr-0 pl-2.5 box-border max-w-full text-black font-kreon">
        <div className="flex-1 flex flex-col items-start justify-start gap-[26px] max-w-full">
          <div className="self-stretch flex flex-col items-start justify-start gap-[23px] max-w-full text-5xl font-arimo-hebrew-subset-italic">
            <div className="self-stretch flex flex-row items-start justify-between gap-[20px] mq450:flex-wrap">
              <i className="relative leading-[150%] [text-shadow:0px_4px_4px_rgba(0,_0,_0,_0.25)] mq450:text-lgi mq450:leading-[29px]">
                {item} ({images.length > 0 ? images[0].dataNumber : ''})
              </i>
              <div className="relative leading-[150%] font-medium inline-block min-w-[14px] mq450:text-base mq450:leading-[24px]">
                <Pagination>
                  <PaginationContent>
                    <PaginationItem>
                      <PaginationPrevious onClick={() => setPage(prevPage => Math.max(prevPage - 1, 1))} />
                    </PaginationItem>
                    {[...Array(5)].map((_, index) => (
                      <PaginationItem
                        key={index}
                        style={{ background: 'none', border: 'none' }}
                      >
                        <PaginationLink
                          href="#"
                          onClick={() => setPage(index + 1)}
                          isActive={index + 1 === page}
                          style={{ background: 'none', border: 'none' }}
                        >
                          {index + 1}
                        </PaginationLink>
                      </PaginationItem>
                    ))}
                    <PaginationItem>
                      <PaginationNext onClick={() => setPage(prevPage => prevPage + 1)} />
                    </PaginationItem>
                  </PaginationContent>
                </Pagination>
              </div>
            </div>
            <div className="self-stretch grid gap-[54px] max-w-full text-xl font-kreon">
              <GalleryItemRow images={images} />
            </div>
            <div className="self-stretch flex flex-row items-start justify-between gap-[20px] mq450:flex-wrap">
              <i className="relative leading-[150%] [text-shadow:0px_4px_4px_rgba(0,_0,_0,_0.25)] mq450:text-lgi mq450:leading-[29px]">
              </i>
              <div className="relative leading-[150%] font-medium inline-block min-w-[14px] mq450:text-base mq450:leading-[24px]">
                <Pagination>
                  <PaginationContent>
                    <PaginationItem>
                      <PaginationPrevious onClick={() => setPage(prevPage => Math.max(prevPage - 1, 1))} />
                    </PaginationItem>
                    {[...Array(5)].map((_, index) => (
                      <PaginationItem
                        key={index}
                        style={{ background: 'none', border: 'none' }}
                      >
                        <PaginationLink
                          href="#"
                          onClick={() => setPage(index + 1)}
                          isActive={index + 1 === page}
                          style={{ background: 'none', border: 'none' }}
                        >
                          {index + 1}
                        </PaginationLink>
                      </PaginationItem>
                    ))}
                    <PaginationItem>
                      <PaginationNext onClick={() => setPage(prevPage => prevPage + 1)} />
                    </PaginationItem>
                  </PaginationContent>
                </Pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default LocationStyle;