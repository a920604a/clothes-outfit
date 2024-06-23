import styles from "./Frame.module.css";
import React, { useState, useCallback } from 'react';
import {
    Box,
    Button,
    Center,
    Spinner,
    Grid,
    Image as ChakraImage,
    Text
} from '@chakra-ui/react';

export const Frame = () => {
    const [filters, setFilters] = useState({ style: '', gender: '', color: '' });
    const [images, setImages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [cancelRequest, setCancelRequest] = useState(false);

    const handleFilterChange = (key, value) => {
        const newFilters = { ...filters, [key]: value };
        setFilters(newFilters);
        setCancelRequest(true); // 取消先前的請求
        setCancelRequest(false); // 開啟新的請求
        fetchImages(newFilters);
    };

    const fetchImages = useCallback(async (newFilters) => {
        setLoading(true);
        try {
            const response = await fetch('http://localhost:8080/api/images', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newFilters),
            });
            if (!cancelRequest) {
                const data = await response.json();
                setImages(data); // 假設 data 是影像的 URL 列表
            }
        } catch (error) {
            console.error('Error fetching images:', error);
        } finally {
            if (!cancelRequest) {
                setLoading(false);
            }
        }
    }, [cancelRequest]);

    return (
        <div className={styles.div}>
            <div className={styles.navigation}>
                <div className={styles.items}>
                    <i className={styles.cooperateWithBeams}>Cooperate with Beams</i>
                </div>
                <div className={styles.styleChoose}>Style Choose</div>
            </div>
            <div className={styles.navigationFooter}>
                <div className={styles.styleChoose1}>Style Choose</div>
                <div className={styles.divider} />
                <div className={styles.items1} />
                <i className={styles.cooperateWithBeams1}>Cooperate with Beams</i>
                <i className={styles.ccclubProject}>ccClub project</i>
                <i className={styles.timvincentjennieellie}>
                    Tim、Vincent、Jennie、Ellie
                </i>
                <img className={styles.image16Icon} alt="" src="/image-16@2x.png" />
            </div>
            {loading ? (
                <Center>
                    <Spinner size="xl" />
                </Center>
            ) : (
                <Grid templateColumns="repeat(auto-fill, minmax(200px, 1fr))" gap={6}>
                    {images.map((image, index) => (
                        <ChakraImage key={index} src={image} alt={`image-${index}`} boxSize="200px" objectFit="cover" />
                    ))}
                </Grid>
            )}
            <div className={styles.style}>
                <div className={styles.div1}>① 選擇地點的風格｜</div>
                <div className={styles.div2} onClick={() => handleFilterChange('style', '工業')}>工業</div>
                <div className={styles.div3} onClick={() => handleFilterChange('style', '日系')}>日系</div>
                <div className={styles.div4} onClick={() => handleFilterChange('style', '極簡')}>極簡</div>
                <div className={styles.div5} onClick={() => handleFilterChange('style', '古典')}>古典</div>
                <div className={styles.div6} onClick={() => handleFilterChange('style', '戶外')}>戶外</div>
                <div className={styles.div7} onClick={() => handleFilterChange('style', '歐洲')}>歐洲</div>
            </div>
            <div className={styles.gender}>
                <div className={styles.div1}>② 選擇性別｜</div>
                <div className={styles.div8} onClick={() => handleFilterChange('gender', '男性')}>男性</div>
                <div className={styles.div2} onClick={() => handleFilterChange('gender', '女性')}>女性</div>
                <div className={styles.div3} onClick={() => handleFilterChange('gender', '不限性別')}>不限性別</div>
            </div>
            <div className={styles.color}>
                <div className={styles.div12}>③ 選擇顏色｜</div>
                <img className={styles.colorChild} alt="yellow" src="/Vector 1.png" onClick={() => handleFilterChange('color', '黃色系')} />
                <img className={styles.colorItem} alt="green" src="/Vector 2.png" onClick={() => handleFilterChange('color', '綠色系')} />
                <img className={styles.colorInner} alt="blue" src="/Vector 3.png" onClick={() => handleFilterChange('color', '藍色系')} />
                <img className={styles.vectorIcon} alt="gray" src="/Vector 4.png" onClick={() => handleFilterChange('color', '灰色系')} />
                <img className={styles.colorChild1} alt="black" src="/Vector 5.png" onClick={() => handleFilterChange('color', '黑色系')} />
                <img className={styles.colorChild2} alt="red" src="/Vector 6.png" onClick={() => handleFilterChange('color', '紅色系')} />
                <img className={styles.colorChild3} alt="orange" src="/Vector 7.png" onClick={() => handleFilterChange('color', '橘色系')} />
                <img className={styles.colorChild4} alt="pink" src="/Vector 8.png" onClick={() => handleFilterChange('color', '粉色系')} />
            </div>
            <div className={styles.div13}>
                <div className={styles.div1}>1</div>
                <div className={styles.div15}>2</div>
                <div className={styles.div16}>3</div>
                <div className={styles.div17}>4</div>
                <div className={styles.div18}>5</div>
                <div className={styles.div19}>{`>`}</div>
            </div>
            <div className={styles.div20}>
                <div className={styles.div1}>1</div>
                <div className={styles.div15}>2</div>
                <div className={styles.div16}>3</div>
                <div className={styles.div17}>4</div>
                <div className={styles.div18}>5</div>
                <div className={styles.div19}>{`>`}</div>
            </div>
            <Text className={styles.popularity200}>Popularity (200)</Text>
        </div>
    );
};

export default Frame;
