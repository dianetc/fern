// This file was auto-generated by Fern from our API Definition.

package api

import (
	bytes "bytes"
	context "context"
	fmt "fmt"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/upload/fixtures/core"
	io "io"
	multipart "mime/multipart"
	http "net/http"
)

type FileClient interface {
	Upload(ctx context.Context, file io.Reader, request *UploadRequest) (string, error)
	UploadSimple(ctx context.Context, file io.Reader) (string, error)
	UploadMultiple(ctx context.Context, file io.Reader, optionalFile io.Reader, request *UploadMultiRequest) (string, error)
}

func NewFileClient(opts ...core.ClientOption) FileClient {
	options := core.NewClientOptions()
	for _, opt := range opts {
		opt(options)
	}
	return &fileClient{
		baseURL:    options.BaseURL,
		httpClient: options.HTTPClient,
		header:     options.ToHeader(),
	}
}

type fileClient struct {
	baseURL    string
	httpClient core.HTTPClient
	header     http.Header
}

func (f *fileClient) Upload(ctx context.Context, file io.Reader, request *UploadRequest) (string, error) {
	baseURL := ""
	if f.baseURL != "" {
		baseURL = f.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return response, err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return response, err
	}
	if err := writer.WriteField("fern", fmt.Sprintf("%v", "fern")); err != nil {
		return response, err
	}
	var statusDefaultValue string
	if request.Status != statusDefaultValue {
		if err := writer.WriteField("status", fmt.Sprintf("%v", request.Status)); err != nil {
			return response, err
		}
	}
	if err := writer.Close(); err != nil {
		return response, err
	}
	f.header.Set("Content-Type", writer.FormDataContentType())

	if err := core.DoRequest(
		ctx,
		f.httpClient,
		endpointURL,
		http.MethodPost,
		requestBuffer,
		&response,
		f.header,
		nil,
	); err != nil {
		return response, err
	}
	return response, nil
}

func (f *fileClient) UploadSimple(ctx context.Context, file io.Reader) (string, error) {
	baseURL := ""
	if f.baseURL != "" {
		baseURL = f.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload-simple"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return response, err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return response, err
	}
	if err := writer.Close(); err != nil {
		return response, err
	}
	f.header.Set("Content-Type", writer.FormDataContentType())

	if err := core.DoRequest(
		ctx,
		f.httpClient,
		endpointURL,
		http.MethodPost,
		requestBuffer,
		&response,
		f.header,
		nil,
	); err != nil {
		return response, err
	}
	return response, nil
}

func (f *fileClient) UploadMultiple(ctx context.Context, file io.Reader, optionalFile io.Reader, request *UploadMultiRequest) (string, error) {
	baseURL := ""
	if f.baseURL != "" {
		baseURL = f.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload-multi"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return response, err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return response, err
	}
	if optionalFile != nil {
		optionalFileFilename := "optionalFile_filename"
		if named, ok := optionalFile.(interface{ Name() string }); ok {
			optionalFileFilename = named.Name()
		}
		optionalFilePart, err := writer.CreateFormFile("optionalFile", optionalFileFilename)
		if err != nil {
			return response, err
		}
		if _, err := io.Copy(optionalFilePart, optionalFile); err != nil {
			return response, err
		}
	}
	var statusDefaultValue string
	if request.Status != statusDefaultValue {
		if err := writer.WriteField("status", fmt.Sprintf("%v", request.Status)); err != nil {
			return response, err
		}
	}
	if err := writer.Close(); err != nil {
		return response, err
	}
	f.header.Set("Content-Type", writer.FormDataContentType())

	if err := core.DoRequest(
		ctx,
		f.httpClient,
		endpointURL,
		http.MethodPost,
		requestBuffer,
		&response,
		f.header,
		nil,
	); err != nil {
		return response, err
	}
	return response, nil
}
