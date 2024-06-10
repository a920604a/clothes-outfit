CREATE DATABASE IF NOT EXISTS closet;
GRANT ALL on closet.* to ccc @'%';
CREATE TABLE IF NOT EXISTS `user`(
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '使用者ID',
    `username`,
    `password`,
    `email`,
    `created_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '創建時間',
,
    `updated_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新時間',
) ROW_FORMAT = Dynamic;
CREATE TABLE IF NOT EXISTS `favorites`(
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `user_id`,
    `clothes_id`,
    `created_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '創建時間',
,
    `updated_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新時間',
);
CREATE TABLE IF NOT EXISTS `clothes`(
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '衣服ID',
    `sex`,
    `color`,
    `category`,
    `image_url`,
    `post_url`,
    `created_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '創建時間',
,
    -- `updated_at` TIMESTAMP(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新時間',
);