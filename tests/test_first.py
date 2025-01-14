from check_os_ver.osver import get_os_version_of_mac

def test_first():
    v = get_os_version_of_mac()

    # 정상적인 값인지
    assert v is not None

    # 빈 문자열이 아닌지
    assert v != ""

    # 문자열에 LTS가 포함 되었는지 -> mac이기 때문에, Darwin이 포함 되었는지로 변경
    # assert "LTS" in v, "'LTS' is not in "
    assert "Darwin" in v

    # 문자열에 문자도 있고, 숫자도 있는지
    assert any(c.isalpha() for c in v)
    assert any(c.isdigit() for c in v)
    
    # . 이 포함 되어있는지
    assert '.' in v

    # 길이가 최소 얼마 이상인지
    assert len(v) > 6

    # 기타 등등
