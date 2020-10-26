class ElevadorJahNoTerreoException(Exception):
    def __init__(self):
        super().__init__("Elevador já está no térreo!")