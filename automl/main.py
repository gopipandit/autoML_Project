from automl.data.data_loader import DataLoader


def main():

    data_loader = DataLoader(r'C:\Users\GopinathPandit\OneDrive - ConcertAI\Python\Pycharm_projects\AUTO_ML_PROJECT\pythonProject\data_samples\land_price.csv')
    data = data_loader.load_data()
    preprocessed_data = data_loader.preprocess_data(data)
    print(preprocessed_data)

if __name__ == '__main__':
    main()