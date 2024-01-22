# frozen_string_literal: true

require_relative "submission/types/SubmissionId"
require "json"

module SeedClient
  module Submission
    class GradedResponseV2
      attr_reader :submission_id, :test_cases, :additional_properties

      # @param submission_id [Submission::SubmissionId]
      # @param test_cases [Hash{V2::Problem::TestCaseId => V2::Problem::TestCaseId}]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [Submission::GradedResponseV2]
      def initialze(submission_id:, test_cases:, additional_properties: nil)
        # @type [Submission::SubmissionId]
        @submission_id = submission_id
        # @type [Hash{V2::Problem::TestCaseId => V2::Problem::TestCaseId}]
        @test_cases = test_cases
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of GradedResponseV2
      #
      # @param json_object [JSON]
      # @return [Submission::GradedResponseV2]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        submission_id Submission::SubmissionId.from_json(json_object: struct.submissionId)
        test_cases struct.testCases.transform_values do |v|
          V2::Problem::TestCaseId.from_json(json_object: v)
        end
        new(submission_id: submission_id, test_cases: test_cases, additional_properties: struct)
      end

      # Serialize an instance of GradedResponseV2 to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { submissionId: @submission_id, testCases: @test_cases.transform_values do |v|
                                                     V2::Problem::TestCaseId.from_json(json_object: v)
                                                   end }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        SubmissionId.validate_raw(obj: obj.submission_id)
        obj.test_cases.is_a?(Hash) != false || raise("Passed value for field obj.test_cases is not the expected type, validation failed.")
      end
    end
  end
end