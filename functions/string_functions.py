def create_alias(name, characters_cz='áéěíóúůýřťžšďčň ', characters_en='aeeiouuyrtzsdcn-', special_characters='-'):
    """
    Create alias from name of item
    Example input: Žluťoučký kůň úpěl ďábelské ódy!
    Exapmle output: zlutoucky-kun-upel-dabelske-ody
    """
    alias = ''
    characters_dict = dict(zip(characters_cz, characters_en))
    list_letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    list_letters += [str(n) for n in range(10)]
    for char in name.lower():
        if char in characters_dict:
            alias += characters_dict[char]
        elif char not in list_letters:
            alias += special_characters
        else:
            alias += char
    return alias
