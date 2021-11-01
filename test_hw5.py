from hw5 import unique

def test_unique():
    assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([]) == []

from hw5 import count_words
def test_count_words():
    assert count_words(["text", "text", "apple", "orange", "yellow", "orange"]) == {
        "text": 2,
        "orange": 2,
        "yellow": 1,
        "apple": 1
    }
    assert count_words(["text", "text", "text", "text", "text", "orange"]) == {
        "text": 5,
        "orange": 1,
    }
    assert count_words([]) == {}

from hw5 import consistent_string
def test_consistent_string():
    assert consistent_string(allowed="ab", strings=["ad", "bd", "aaab", "baa", "badab"]) == {"aaab", "baa"}
    assert consistent_string(allowed="abc", strings=["a", "b", "c", "ab", "ac", "bc", "abc"]) == {"a", "b", "c", "ab",
                                                                                                  "ac", "bc", "abc"}
    assert consistent_string(allowed="cad", strings=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == {"cc", "acd",
                                                                                                           "ac", "d"}

from hw5 import sort_desc
def test_sort_desc():
    assert sort_desc(["ad", "bd", "aaab", "baa", "badab"]) == ['bd', 'badab', 'baa', 'ad', 'aaab']
    assert sort_desc(["a", "b", "c", "ab", "ac", "bc", "abc"]) == ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a']

from hw5 import filter_even
def test_filter_even():
    assert filter_even([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) == [2, 4, 6, 8, 10, 12]
    assert filter_even([2, 2, 4, 6, 6, 8, 10, 12]) == [2, 2, 4, 6, 6, 8, 10, 12]
    assert filter_even([1, 1, 2, 3]) == [2]
    assert filter_even([1, 3, 5]) == []



