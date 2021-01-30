def read_grid_from_file(file_path):
    pass  # TODO: implement


def write_grid_to_file(grid, file_path):
    f = open("file_path.txt", "w", encoding='utf-8')
    for line in [''.join(i) for i in grid]:
        f.write(line + '\n')
    f.close()
