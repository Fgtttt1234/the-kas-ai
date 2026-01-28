#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test and demonstration of the identity system
This script demonstrates all the ways to use the identity module
"""

from core import identity, banner, NAME_AR, NAME_EN, FOUNDER, FOUNDED
from core.identity import get_full_name, get_description


def test_constants():
    """Test accessing identity constants."""
    print("=" * 70)
    print("Testing Identity Constants")
    print("=" * 70)
    print(f"Arabic Name:  {NAME_AR}")
    print(f"English Name: {NAME_EN}")
    print(f"Founder:      {FOUNDER}")
    print(f"Founded:      {FOUNDED}")
    print()


def test_identity_function():
    """Test the identity() function that returns all data."""
    print("=" * 70)
    print("Testing identity() Function")
    print("=" * 70)
    id_data = identity()
    for key, value in id_data.items():
        print(f"{key:20s}: {value}")
    print()


def test_banner_arabic():
    """Test the Arabic banner."""
    print("=" * 70)
    print("Testing Arabic Banner")
    print("=" * 70)
    print(banner("ar"))
    print()


def test_banner_english():
    """Test the English banner."""
    print("=" * 70)
    print("Testing English Banner")
    print("=" * 70)
    print(banner("en"))
    print()


def test_helper_functions():
    """Test helper functions."""
    print("=" * 70)
    print("Testing Helper Functions")
    print("=" * 70)
    print(f"Full Name (AR): {get_full_name('ar')}")
    print(f"Full Name (EN): {get_full_name('en')}")
    print(f"Description (AR): {get_description('ar')}")
    print(f"Description (EN): {get_description('en')}")
    print()


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("Identity System Test Suite")
    print("مجموعة اختبارات نظام الهوية")
    print("=" * 70 + "\n")
    
    test_constants()
    test_identity_function()
    test_banner_arabic()
    test_banner_english()
    test_helper_functions()
    
    print("=" * 70)
    print("All tests completed successfully!")
    print("جميع الاختبارات اكتملت بنجاح!")
    print("=" * 70)


if __name__ == "__main__":
    main()
