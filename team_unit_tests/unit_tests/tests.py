from unittest import TestCase, main

from team_unit_tests.project.team import Team


class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("MyTeam")

    def test_init(self):
        name = "MyTeam"
        team = Team(name)

        self.assertEqual(name, team.name)
        self.assertEqual({}, self.team.members)

    def test_if_name_contains_only_letters(self):
        name = "MyTeam"
        self.assertEqual(name, self.team.name)

    def test_if_name_does_not_contains_only_letters(self):
        with self.assertRaises(ValueError) as ex:
            Team("MyTeAm123!@*")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_if_member_not_in_team(self):
        self.team.members["ivan"] = 18
        result = self.team.add_member(ivan=12, gosho=13, pesho=16)

        self.assertEqual("Successfully added: gosho, pesho", result)
        self.assertEqual(13, self.team.members["gosho"])
        self.assertEqual(16, self.team.members["pesho"])
        self.assertEqual(3, len(self.team.members))

    def test_remove_member_if_member_exists(self):
        self.team.members["ivan"] = 18
        result = self.team.remove_member("ivan")
        expected = "Member ivan removed"
        self.assertEqual(expected, result)
        self.assertEqual(0, len(self.team.members))

    def test_remove_member_if_member_does_not_exists(self):
        result = self.team.remove_member("Pesho")
        expected = "Member with name Pesho does not exist"
        self.assertEqual(expected, result)
        self.assertEqual(0, len(self.team))
        self.assertTrue("Pesho" not in self.team.members)


    def test_if_team_greater_than_other_team(self):
        self.team.members["member_1"] = 12
        self.team.members["member_2"] = 15
        self.team.members["member_3"] = 13

        another_team = Team("Another")
        another_team.members["member_4"] = 11
        another_team.members["member_5"] = 10

        self.assertEqual(True, self.team > another_team)
        self.assertEqual(False, another_team > self.team)

    def test_len_members(self):
        self.team.members["member_1"] = 12
        self.team.members["member_2"] = 15
        self.team.members["member_3"] = 13
        self.assertEqual(3, len(self.team))

    def test_add_returns_new_team(self):
        self.team.members["member_1"] = 12
        self.team.members["member_2"] = 15
        self.team.members["member_3"] = 13

        another_team = Team("Another")
        another_team.members["member_4"] = 11
        another_team.members["member_5"] = 10

        expected_team = self.team + another_team
        result = {
            "member_1": 12,
            "member_2": 15,
            "member_3": 13,
            "member_4": 11,
            "member_5": 10,

        }

        self.assertEqual("MyTeamAnother", expected_team.name)
        self.assertEqual(result, expected_team.members)

    def test_if_str_returns_proper_string_in_descending_order(self):
        self.team.members["member_1"] = 12
        self.team.members["member_2"] = 15
        self.team.members["member_3"] = 13

        actual = str(self.team)
        expected = f"Team name: MyTeam\n" +\
        f"Member: member_2 - 15-years old\n" +\
        f"Member: member_3 - 13-years old\n" + \
        f"Member: member_1 - 12-years old"

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()


