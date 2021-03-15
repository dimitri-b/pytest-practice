
def test_tmpdir(tmpdir):
    """Test built-in tmpdir fixture features"""
    # tmpdir is an auto-generated path object to a temp location
    # it has 'function' scope and doesn't persist beyond the calling function

    # it can be used to create a path to a file
    file_1 = tmpdir.join('foo.txt')

    # also a sub-dir
    dir_1 = tmpdir.mkdir('some_files')

    # subdir is of the same type as tmpdir
    file_2 = dir_1.join("bar.txt")

    # files will be created when written to
    file_1.write("just testing...")
    file_2.write("still testing...")

    assert file_1.read() == "just testing..."
    assert file_2.read() == "still testing..."


def test_tmpdir_factory(tmpdir_factory):
    """Test built-in tmpdir_factory fixture features"""
    # tmpdir_factory has a session scope

    # base directory, in case it is needed (picked automatically)
    # can also be specified
    base_dir = tmpdir_factory.getbasetemp()
    print("\nbase:", base_dir)

    # tmpdir_factory is not a directory, but is used to create subdirs under base
    dir_3 = tmpdir_factory.mktemp('some_more_files')

    # subdir is of the same type as tmpdir
    file_3 = dir_3.join("baz.txt")

    # files will be created when written to
    file_3.write("another test...")

    assert file_3.read() == "another test..."
