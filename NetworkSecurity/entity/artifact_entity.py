from dataclasses import dataclass

# this dataclass acts like decorator which creates variable for empty class
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str