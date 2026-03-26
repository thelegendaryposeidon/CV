from sqlalchemy import create_engine, inspect

# Use your actual connection details here
# Format: postgresql://user:password@localhost:5432/dbname
db_url = "postgresql://postgres:password@localhost:5432/cvdb"

engine = create_engine(db_url)

def check_columns():
    inspector = inspect(engine)
    try:
        columns = inspector.get_columns('constituencies_pc')
        
        print(f"\n{'Column Name':<25} | {'Data Type':<15}")
        print("-" * 45)
        
        if not columns:
            print("No columns found. Is the table name 'constituencies_pc' correct?")
            return

        for column in columns:
            print(f"{column['name']:<25} | {str(column['type']):<15}")
            
    except Exception as e:
        print(f"Failed to inspect table: {e}")

if __name__ == "__main__":
    check_columns()