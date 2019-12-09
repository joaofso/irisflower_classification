from sklearn.model_selection import train_test_split


class Classifier:

    def __init__(self, data, input_attributes, response_attribute, selection_technique):
        if not self.__contains_attributes(data, input_attributes, response_attribute):
            raise Exception('There are invalid attributes')
        self.data = data
        self.input_attr = input_attributes
        self.response_attr = response_attribute
        self.model = selection_technique

    def __contains_attributes(self, data, input_attributes, response_attribute):
        attributes = input_attributes + response_attribute
        return all(x in data.columns for x in attributes)

    def __valid_train_proportion(self, train_proportion):
        try:
            proportion = float(train_proportion)
            return 0 < proportion < 1
        except ValueError:
            return False

    def train(self, train_proportion):
        if not self.__valid_train_proportion(train_proportion):
            raise Exception('The proportion of samples for training is not a valid number. Please provide a number '
                            'between 0 and 1')
        __X_train, __X_test, __Y_train, __Y_test = train_test_split(self.data[self.input_attr],
                                                                    self.data[self.response_attr],
                                                                    train_size=train_proportion)
        self.model.fit(__X_train, __Y_train)
        return {'train': self.model.score(__X_train, __Y_train), 'test': self.model.score(__X_test, __Y_test)}
