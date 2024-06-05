import csv
from ExtractManagement import ExtractManagement


class CSVExtractManagement(ExtractManagement):
    def extract(self, source):
        with open(source, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data

    def transform(self, data):
        # 這裡進行簡單的轉換，例如將所有字符串轉為大寫
        transformed_data = [{k: v.upper() if isinstance(v, str) else v for k, v in row.items()} for row in data]
        return transformed_data

    def load(self, data, destination):
        if data:
            keys = data[0].keys()
            with open(destination, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)


# 使用範例
# extractor = CSVExtractManagement()
# data = extractor.extract('input.csv')
# transformed_data = extractor.transform(data)
# extractor.load(transformed_data, 'output.csv')
