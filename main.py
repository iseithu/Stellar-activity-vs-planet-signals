from src.data_simulation import generate_data

def main():
    data = generate_data()
    print("Data generated:", data.shape)

if __name__ == "__main__":
    main()
